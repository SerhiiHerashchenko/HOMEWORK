function lab2_var12
    clc; close all;

    % Параметры варианта 12 (предполагаемые)
    a = 0;
    b = pi;
    n = 20;
    eps_noise = 0.1;

    m_list = [3, 5, 10];

    x = a + rand(1, n) * (b - a);
    x = sort(x);

    fv_exact = f(x);

    fv_noisy = fv_exact;
    for i = 1:n
        noise = eps_noise * (-1 + 2 * rand());
        fv_noisy(i) = fv_noisy(i) + noise * abs(fv_noisy(i));
    end

    fprintf('=== ВАРИАНТ 12: f(x) = x * cos(x) ===\n');
    fprintf('%-5s | %-15s\n', 'm', 'cond(A)');
    fprintf('-----------------------\n');

    for k = 1:length(m_list)
        m = m_list(k);

        A = zeros(n, m + 1);
        for i = 1:n
            A(i, 1) = 1;
            for j = 1:m
                A(i, j + 1) = x(i)^j;
            end
        end

        g = fv_noisy';

        [U, S, V] = svd(A);
        s_vals = diag(S);
        condA = max(s_vals) / min(s_vals);

        fprintf('%-5d | %-15.4e\n', m, condA);

        u = A \ g;
        u_poly = u(end:-1:1);

        figure(k + 3); % Чтобы не перекрывать графики варианта 4
        nn = 200;
        h = (b - a) / nn;
        xt = a:h:b;
        ft = f(xt);
        fa = polyval(u_poly, xt);

        plot(xt, ft, 'k-', 'LineWidth', 1.5); hold on;
        plot(x, fv_noisy, 'mo', 'MarkerFaceColor', 'm');
        plot(xt, fa, 'g--', 'LineWidth', 2);

        title(['Var 12: Approx m = ' num2str(m) ', cond(A) = ' num2str(condA, '%.2e')]);
        legend('f(x)', 'Noisy data', 'LSM Polynomial');
        grid on;
    end
end

function y = f(x)
    % Вариант 12 (Предположительный, так как нет в таблице)
    % По структуре похож на вар. 6 и 7.
    y = x .* cos(x);
end
