function lab1_var12
    % Очистка
    clc;

    nn = [5 10 15 20 50 75 100 150 200];

    for ob = [1, 0]
        if ob == 1
            fprintf('\n=== РЕЗУЛЬТАТЫ ДЛЯ ДОБРЕ ОБУМОВЛЕНОЇ МАТРИЦІ (DOM) ===\n');
        else
            fprintf('\n=== РЕЗУЛЬТАТЫ ДЛЯ ПОГАНО ОБУМОВЛЕНОЇ МАТРИЦІ (POM) ===\n');
        end

        fprintf('%-5s | %-10s | %-12s | %-12s | %-12s\n', 'n', 'cond(A)', 'Err Rel', 'Aposteriori', 'Refined Err');
        fprintf('------------------------------------------------------------------\n');

        for i = 1:length(nn)
            n = nn(i);

            A = initA(ob, n);

            condA_inf = cond(A, inf);
            condA_1 = cond(A, 1);

            x_t = rand(n, 1);
            b = A * x_t;

            % Решение через PLU
            x = Solve(A, b);

            r = b - A * x';

            absAx = abs(A) * abs(x');
            cond_check = condA_inf * max(absAx) / min(absAx) * eps(1);

            if cond_check < 1
                dx = Solve(A, r);
                xi = x - dx;
            else
                xi = x;
            end

            ri = b - A * xi';
            rel_err = norm(x_t - xi', 1) / norm(xi, 1);
            apost_est = (condA_1 / norm(A, 1)) * norm(ri, 1) / norm(xi, 1);

            fprintf('%-5d | %-10.2e | %-12.2e | %-12.2e | %-12.2e\n', ...
                n, condA_1, rel_err, apost_est, norm(x_t - xi', 1));
        end
    end
end

% Функция инициализации (DOM #6 / POM #2)
function A = initA(ob, n)
    if ob == 1
        % DOM 6: Специфическая формула
        A = zeros(n);
        for i = 1:n
            for j = 1:n
                if i == j
                    A(i, j) = 1;
                elseif i < j
                    A(i, j) = 1 / n;
                else
                    A(i, j) = -1 / n;
                end
            end
        end
    else
        % POM 2: Матрица Лоткина
        % Используем gallery('lotkin', n)
        A = gallery('lotkin', n);

        % Если gallery нет, вот формула Лоткина:
        % Первая строка - все 1. Остальные a_ij = 1/(i+j-1)
        % for i=1:n
        %   A(1,i)=1;
        %   for j=1:n
        %      if i>1, A(i,j)=1/(i+j-1); end
        %   end
        % end
    end
end

% Функция PLU разложения (из твоего шаблона)
function [p, L, U] = my_LU(A)
    n = size(A, 1);
    p = 1:n; % Вектор перестановок (в шаблоне p(:,1), упростил до вектора)
    L = eye(n);
    U = zeros(n);

    for k = 1:n-1
        % Выбор главного элемента
        [~, km] = max(abs(A(k:n, k)));
        km = km + k - 1;

        if km > k
            % Обмен строк в A
            A([k, km], :) = A([km, k], :);
            % Обмен в векторе перестановок
            p([k, km]) = p([km, k]);

            % Обмен в L (той части, что уже вычислена, слева от k)
            if k > 1
                L([k, km], 1:k-1) = L([km, k], 1:k-1);
            end
        end

        if A(k, k) == 0
            % Предотвращение деления на ноль, хотя для Lotkin/DOM это редкость
            A(k,k) = eps;
        end

        for i = k+1:n
            N = A(i, k) / A(k, k);
            L(i, k) = N; % Записываем множитель в L
            A(i, k+1:n) = A(i, k+1:n) - N * A(k, k+1:n);
        end
    end

    % U - это верхняя треугольная часть A
    U = triu(A);
end


function [x] = Solve(A, b)
    [p, L, U] = my_LU(A);
    n = size(A, 1);

    % Применяем перестановки к вектору b
    b = b(p);

    x = zeros(1, n);
    y = zeros(1, n);

    % Прямой ход: Ly = b
    % У L на диагонали 1, поэтому делить не нужно
    y(1) = b(1);
    for i = 2:n
        s = b(i);
        for j = 1:i-1
            s = s - y(j) * L(i, j);
        end
        y(i) = s; % / L(i,i) не нужно, так как L(i,i)=1
    end

    % Обратный ход: Ux = y
    x(n) = y(n) / U(n, n);
    for i = n-1:-1:1
        s = y(i);
        for j = i+1:n
            s = s - x(j) * U(i, j);
        end
        x(i) = s / U(i, i);
    end
end
