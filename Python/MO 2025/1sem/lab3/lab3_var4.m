function lab3_var4
    clc; close all;

    % Параметры для Варианта 4
    nx = 6;
    ny = 6;

    % Точность e^-10
    eps_val = exp(-10);

    % 1. Формирование матрицы
    A = gallery('wathen', nx, ny);
    n = size(A, 1);

    fprintf('=== ВАРИАНТ 4 (nx=%d, ny=%d, size=%dx%d) ===\n', nx, ny, n, n);

    % 2. Спектральный анализ
    opts.tol = 1e-6;
    % ИСПРАВЛЕНИЕ: Используем 'LM' и 'SM' вместо 'largestabs'/'smallestabs'
    M = eigs(A, 1, 'LM', opts);
    m = eigs(A, 1, 'SM', opts);

    % M и m могут вернуться как векторы или матрицы 1x1, берем значения
    M = abs(M(1));
    m = abs(m(1));

    condA = M / m;

    % 3. Теоретические оценки сходимости
    nu_iter_theor = (M - m) / (M + m);
    nu_rich_theor = (sqrt(condA) - 1) / (sqrt(condA) + 1);

    % 4. Модельная задача
    x_true = rand(n, 1);
    b = A * x_true;
    x0_start = zeros(n, 1);

    fprintf('\n%-10s | %-10s | %-10s | %-5s | %-8s | %-10s\n', ...
        'cond(A)', 'nu_iter', 'nu_rich', 'p', 'k (iter)', 'nu (fact)');
    fprintf('%s\n', repmat('-', 1, 70));

    pp = [1, 5, 10, 20];

    figure(1); hold on; grid on;
    colors = ['r', 'g', 'b', 'k'];
    styles = {'-o', '-s', '-^', '-d'};

    for idx = 1:length(pp)
        p = pp(idx);

        alpha = zeros(1, p);
        for i = 0:p-1
            root_cheb = (M + m)/2 + ((M - m)/2) * cos((2*i + 1)*pi / (2*p));
            alpha(i+1) = 1 / root_cheb;
        end

        x = x0_start;
        k = 0;
        err_history = [];
        initial_err = norm(x - x_true);

        while true
            for j = 1:p
                r = A*x - b;
                x = x - alpha(j) * r;
            end
            k = k + p;

            curr_err = norm(x - x_true);
            err_history(end+1) = curr_err;

            if curr_err <= eps_val * initial_err
                break;
            end

            if k > 50000
                fprintf(' No conv p=%d ', p);
                break;
            end
        end

        nu_fact = (curr_err / initial_err)^(1/k);

        if idx == 1
            fprintf('%-10.2e | %-10.4f | %-10.4f | %-5d | %-8d | %-10.4f\n', ...
                condA, nu_iter_theor, nu_rich_theor, p, k, nu_fact);
        else
            fprintf('%-10s | %-10s | %-10s | %-5d | %-8d | %-10.4f\n', ...
                '', '', '', p, k, nu_fact);
        end

        iter_axis = p:p:k;
        semilogy(iter_axis, err_history, [styles{idx} colors(idx)], ...
            'DisplayName', sprintf('p=%d', p), 'MarkerSize', 4);
    end

    xlabel('Iterations (k)');
    ylabel('Error ||x_k - x^*||');
    title(sprintf('Var 4: Convergence (cond=%.1e)', condA));
    legend('show');
end
