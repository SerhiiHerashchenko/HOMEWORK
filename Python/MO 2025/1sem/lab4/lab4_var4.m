function lab4_var4_manual
    clc;

    % Объявляем глобальные переменные, чтобы их видела функция Ax
    global A
    global L

    base_nx = 6;
    base_ny = 6;
    multipliers = [1, 2, 4, 8];

    fprintf('=== ВАРИАНТ 4: Manual CG vs PCG ===\n');
    fprintf('%-15s | %-10s | %-15s | %-15s\n', 'nx, ny', 'n=size(A)', 'k (CG)', 'k (PCG)');
    fprintf('------------------------------------------------------------------\n');

    for m = multipliers
        nx = base_nx * m;
        ny = base_ny * m;

        % 1. Инициализация матрицы A
        A = gallery('wathen', nx, ny);
        n = size(A, 1);

        % Модельная задача
        x_exact = rand(n, 1);
        b = A * x_exact;

        % --- ЭКСПЕРИМЕНТ 1: Обычный CG (без предобуславливания) ---
        % Чтобы использовать тот же код, сделаем L единичной матрицей.
        % Тогда L\b = b и Ax превращается просто в A*x.
        L = speye(n);

        % Запускаем ручной метод
        k_cg = solve_manual(b);

        % --- ЭКСПЕРИМЕНТ 2: PCG (C неполным Холецким) ---
        % Строим предобуславливатель
        % Используем ichol (современный аналог cholinc)
        L = ichol(A);

        % Запускаем ручной метод
        k_pcg = solve_manual(b);

        % Вывод в таблицу
        size_str = sprintf('%d, %d', nx, ny);
        fprintf('%-15s | %-10d | %-15d | %-15d\n', size_str, n, k_cg, k_pcg);
    end
end

function k = solve_manual(b)
    % Функция реализует метод сопряженных градиентов по твоему шаблону
    global A
    global L

    eps_val = 1.0e-6;
    n = size(A, 1);

    % Начальное приближение (нулевое)
    x0 = zeros(n, 1);

    % В предобусловленном методе мы решаем преобразованную систему.
    % Начальная невязка: r0 = L^(-1) * b (для x0=0)
    r0 = L \ b;

    r00_norm = norm(r0, 2); % Запоминаем норму начальной невязки

    p1 = r0; % Начальное направление

    k = 0;

    % Твой цикл while 1==1
    while true
        k = k + 1;

        % q = A * p1 (в преобразованных координатах: L^-T * A * L^-1 * p1)
        q = Ax(p1);

        % Расчет шага alpha
        % alpha = (r0'*r0) / (p1'*q);
        % В твоем шаблоне было (q'*r0), но для CG правильно (p1'*q)
        alpha = (r0' * r0) / (p1' * q);

        x1 = x0 + alpha * p1;
        r1 = r0 - alpha * q;

        % Проверка на выход
        if norm(r1, 2) < r00_norm * eps_val
            break;
        end

        % Расчет beta (по формуле из твоего шаблона - ортогонализация)
        % beta = -(q' * r1) / (q' * p1);
        % Либо классическая формула Fletcher-Reeves: (r1'*r1)/(r0'*r0)
        % Используем ту, что была у тебя в шаблоне:
        beta = -(q' * r1) / (q' * p1);

        p2 = r1 + beta * p1;

        % Обновление переменных для следующего шага
        x0 = x1;
        r0 = r1;
        p1 = p2;

        % Защита от зацикливания
        if k > 20000
            k = -1; % Индикатор расходимости
            break;
        end
    end
end

function y = Ax(x)
    % Вспомогательная функция из шаблона
    global A
    global L

    % Вычисляет y = L^(-T) * A * L^(-1) * x
    y = L' \ x;
    x_temp = A * y;
    y = L \ x_temp;
end
