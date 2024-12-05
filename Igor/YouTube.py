import yt_dlp # Импорт библиотеки в программу.

url = 'https://www.youtube.com/watch?v=XXYlFuWEuKI' #задаем ссылку на видео, в переменной ur1

yd1_opts = {
    'format': 'best', # выбираем лучший формат видео
    'outtmp1': '%(title)s.%(ext)s' #Шаблон имени файла
}

with yt_dlp.YoutubeDL(yd1_opts) as yd1: # with для открытия объекта YoutubeDL, который будет управлять процессом скачивания видео, передаем опцию ydl_opts), чтобы он знал, в каком формате и как сохранять видео
    yd1.download([url]) #Метод download() используется для загрузки видео. Он принимает список ссылок (в нашем случае мы передаем одну ссылку на видео)