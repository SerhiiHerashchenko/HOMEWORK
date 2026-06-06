function lab2_var4
    clc; close all;

    % Параметры варианта 4
    a = 0;
    b = pi;
    n = 20;
    eps_noise = 0.1;

    % Степени аппроксимирующего многочлена (из задания)
    m_list = [3, 5, 10];

    % Генерация узлов и функции
    % Случайные узлы, отсортированные по возрастанию
    x = a + rand(1, n) * (b - a);
    x = sort(x);

    % Точные значения функции
    fv_exact = f(x);

    % Добавляем шум согласно формуле в задании
    % f~(x) = f(x) + eps * rand(-1,1) * |f(x)|
    fv_noisy = fv_exact;
    for i = 1:n
        noise = eps_noise * (-1 + 2 * rand());
        fv_noisy(i) = fv_noisy(i) + noise * abs(fv_noisy(i));
    end

    fprintf('=== ВАРИАНТ 4: f(x) = x + sin(x) ===\n');
    fprintf('%-5s | %-15s\n', 'm', 'cond(A)');
    fprintf('-----------------------\n');

    % Цикл по степеням полинома
    for k = 1:length(m_list)
        m = m_list(k);

        % Формирование матрицы Вандермонда (переопределенной системы)
        % Базис: 1, x, x^2, ..., x^m
        A = zeros(n, m + 1);
        for i = 1:n
            A(i, 1) = 1;
            for j = 1:m
                A(i, j + 1) = x(i)^j;
            end
        end

        g = fv_noisy';

        % SVD разложение для анализа числа обусловленности
        [U, S, V] = svd(A);
        s_vals = diag(S);

        % Число обусловленности (max singular value / min singular value)
        condA = max(s_vals) / min(s_vals);

        fprintf('%-5d | %-15.4e\n', m, condA);

        % Решение СЛАУ методом наименьших квадратов (оператор \)
        u = A \ g;

        % Переворачиваем коэффициенты для polyval (от старшей степени к младшей)
        u_poly = u(end:-1:1);

        % Построение графиков
        figure(k);
        nn = 200; % точек для гладкого графика
        h = (b - a) / nn;
        xt = a:h:b;
        ft = f(xt);          % Точная функция на густой сетке
        fa = polyval(u_poly, xt); % Аппроксимация

        plot(xt, ft, 'k-', 'LineWidth', 1.5); hold on;
        plot(x, fv_noisy, 'bo', 'MarkerFaceColor', 'b');
        plot(xt, fa, 'r--', 'LineWidth', 2);

        title(['Approximation m = ' num2str(m) ', cond(A) = ' num2str(condA, '%.2e')]);
        legend('f(x) точная', 'Точки с шумом', 'Полином МНК');
        xlabel('x'); ylabel('y');
        grid on;
    end
end

function y = f(x)
    % Вариант 4
    y = x + sin(x);
end
