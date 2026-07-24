import time


class LockTime:
    root = None

    @classmethod
    def init(cls, root_window):
        """Сохраняет прямую ссылку на главное окно Tkinter для обновлений."""
        cls.root = root_window

    @classmethod
    def wait(cls, seconds: float):
        """Честная линейная пауза матча на time.time().
        Останавливает чтение кода на одной строчке, но принудительно
        заставляет Tkinter плавно отрисовывать анимации и плашки.
        """
        # Вычисляем точную метку системного времени, когда пауза должна закончиться
        end_time = time.time() + seconds

        while time.time() < end_time:
            # На каждом микро-шаге ожидания заставляем окно перерисовать пиксели
            cls.root.update()

            # Разгружаем процессор на 1 миллисекунду, чтобы ядро не грелось в пустом цикле
            time.sleep(0.01)
