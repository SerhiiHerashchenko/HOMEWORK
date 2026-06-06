function lab1_var4_final
    clc; close all;
    fprintf('Метод Холецького (LL^T) + Графіки\n\n');

    nn = [5 10 15 20 50 75 100 150 200];

    % Массивы для хранения данных для графиков
    data_dom.cond = []; data_dom.err = [];
    data_pom.cond = []; data_pom.err = [];

    % Запускаем два раза: для DOM (ob=1) и для POM (ob=0)
    for ob = [1, 0]
        if ob == 1
            fprintf('\n--- ДОБРЕ ОБУМОВЛЕНА МАТРИЦЯ (DOM #2: Kahan) ---\n');
        else
            fprintf('\n--- ПОГАНО ОБУМОВЛЕНА МАТРИЦЯ (POM #1: Hilbert) ---\n');
        end

        fprintf('%-5s | %-10s | %-12s | %-12s | %-12s\n', ...
            'n', 'cond1(A)', 'Err Rel (x)', 'Aposteriori', 'Err Rel (xi)');
        fprintf('%s\n', repmat('-', 1, 65));

        current_cond = [];
        current_err = [];

        for i = 1:length(nn)
            n = nn(i);

            % 1. Инициализация
            A = initA(ob, n);
            x_exact = rand(n, 1);
            b = A * x_exact;

            condA_1 = cond(A, 1);
            normA_1 = norm(A, 1);

            % 2. Решение (Холецкий)
            x = Solve_Chol(A, b);
            x = x(:);

            % Погрешность
            err_rel_x = norm(x - x_exact, 1) / norm(x, 1);

            % Сохраняем для графика
            current_cond(end+1) = condA_1;
            current_err(end+1) = err_rel_x;

            % 3. Невязка и уточнение
            r = b - A * x;

            % Формула проверки из методички
            abs_prod = abs(A) * abs(x);
            check_val = (max(abs_prod) / min(abs_prod)) * eps;

            if check_val < 1
                dx = Solve_Chol(A, r);
                xi = x + dx(:);
            else
                xi = x;
            end

            err_rel_xi = norm(xi - x_exact, 1) / norm(xi, 1);

            % Апостериорная оценка
            term_invA = condA_1 / normA_1;
            apost_bound = term_invA * (norm(r, 1) / norm(x, 1));

            fprintf('%-5d | %-10.2e | %-12.2e | %-12.2e | %-12.2e\n', ...
                n, condA_1, err_rel_x, apost_bound, err_rel_xi);
        end

        % Сохраняем данные в структуру
        if ob == 1
            data_dom.cond = current_cond;
            data_dom.err = current_err;
        else
            data_pom.cond = current_cond;
            data_pom.err = current_err;
        end
    end

    % --- ПОСТРОЕНИЕ ГРАФИКОВ ---
    figure('Name', 'Dependence Error vs Condition Number', 'Color', 'w');

    % График для DOM
    subplot(1, 2, 1);
    loglog(data_dom.cond, data_dom.err, '-bo', 'LineWidth', 2, 'MarkerSize', 6);
    grid on;
    xlabel('Число обумовленості cond(A)');
    ylabel('Відносна похибка ||x - x^*|| / ||x||');
    title('DOM (Добре обумовлена)');

    % График для POM
    subplot(1, 2, 2);
    loglog(data_pom.cond, data_pom.err, '-r^', 'LineWidth', 2, 'MarkerSize', 6);
    grid on;
    xlabel('Число обумовленості cond(A)');
    ylabel('Відносна похибка ||x - x^*|| / ||x||');
    title('POM (Погано обумовлена)');

    sgtitle('Варіант 4: Залежність похибки від числа обумовленості');
end

function A = initA(ob, n)
    if ob == 1
        % DOM 2: Kahan
        [I, J] = meshgrid(1:n, 1:n);
        A = 0.5 .^ abs(I - J);
    else
        % POM 1: Hilbert
        A = zeros(n);
        for i = 1:n
            for j = 1:n
                A(i, j) = 1 / (i + j - 1);
            end
        end
    end
end

function x = Solve_Chol(A, b)
    n = size(A, 1);
    L = zeros(n);
    for k = 1:n
        sum_val = 0;
        for j = 1:k-1
            sum_val = sum_val + L(k, j)^2;
        end
        val = A(k, k) - sum_val;
        if val <= 0, val = abs(val) + 1e-10; end
        L(k, k) = sqrt(val);
        for i = k+1:n
            sum_val = 0;
            for j = 1:k-1
                sum_val = sum_val + L(i, j) * L(k, j);
            end
            L(i, k) = (A(i, k) - sum_val) / L(k, k);
        end
    end
    U = L';
    y = zeros(n, 1);
    for i = 1:n
        s = b(i);
        for j = 1:i-1
            s = s - L(i, j) * y(j);
        end
        y(i) = s / L(i, i);
    end
    x = zeros(n, 1);
    for i = n:-1:1
        s = y(i);
        for j = i+1:n
            s = s - U(i, j) * x(j);
        end
        x(i) = s / U(i, i);
    end
end
