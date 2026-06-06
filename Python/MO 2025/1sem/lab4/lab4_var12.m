function lab4_var12_manual
    clc;

    global A
    global L

    % Используем параметры Варианта 2, так как 12-го нет в списке
    base_nx = 4;
    base_ny = 4;
    multipliers = [1, 2, 4, 8];

    fprintf('=== ВАРИАНТ 12 (Base Var 2): Manual CG vs PCG ===\n');
    fprintf('%-15s | %-10s | %-15s | %-15s\n', 'nx, ny', 'n=size(A)', 'k (CG)', 'k (PCG)');
    fprintf('------------------------------------------------------------------\n');

    for m = multipliers
        nx = base_nx * m;
        ny = base_ny * m;

        A = gallery('wathen', nx, ny);
        n = size(A, 1);

        x_exact = rand(n, 1);
        b = A * x_exact;

        % 1. Обычный CG (L = Identity)
        L = speye(n);
        k_cg = solve_manual(b);

        % 2. PCG (L = ichol)
        L = ichol(A);
        k_pcg = solve_manual(b);

        size_str = sprintf('%d, %d', nx, ny);
        fprintf('%-15s | %-10d | %-15d | %-15d\n', size_str, n, k_cg, k_pcg);
    end
end

function k = solve_manual(b)
    global A
    global L

    eps_val = 1.0e-6;
    n = size(A, 1);
    x0 = zeros(n, 1);

    % Инициализация: r0 = L\b
    r0 = L \ b;
    r00_norm = norm(r0, 2);
    p1 = r0;
    k = 0;

    while true
        k = k + 1;

        q = Ax(p1);

        alpha = (r0' * r0) / (p1' * q);

        x1 = x0 + alpha * p1;
        r1 = r0 - alpha * q;

        if norm(r1, 2) < r00_norm * eps_val
            break;
        end

        % Формула beta из шаблона
        beta = -(q' * r1) / (q' * p1);

        p2 = r1 + beta * p1;

        x0 = x1;
        r0 = r1;
        p1 = p2;

        if k > 20000, k = -1; break; end
    end
end

function y = Ax(x)
    global A
    global L
    y = L' \ x;
    x_temp = A * y;
    y = L \ x_temp;
end
