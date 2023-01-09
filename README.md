## Курсовая работа по предмету "Системный анализ информационных технологий"
|Вариант|Метод создания карты|Учет  проходимости|Размер робота|Радиус поворота|Видимость  |Алгоритм|   
|-------|--------------------|------------------|-------------|---------------|-----------|--------|
|**23** |Ручная              |Да                |Квадратный   |Нет            |Бесконечная|B*      |

### CLI
```
--algorithm #Алгоитм поиска [astar, bstar, bfs]
--grid      #Тип карты [big2, big, obstacle, empty]
--start     #Точка старта
--finish    #Точка финиша
```

### Примеры запуска
```bash
python3 main.py --algorithm astar --grid big --start 1 1 --finish 13 13
```
<image src="./screenshots/Figure_1_a*.png" caption="B*">

```bash
python3 main.py --algorithm bstar --grid big --start 1 1 --finish 13 13
```
<image src="./screenshots/Figure_1_b*.png" caption="A*">

```bash
python3 main.py --algorithm bfs --grid obstacle --start 0 0 --finish 7 7
```
<image src="./screenshots/Figure_1_bfs.png" caption="B*">
