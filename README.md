## Курсовая работа по предмету "Системный анализ информационных технологий"
|Вариант|Метод создания карты|Учет  проходимости|Размер робота|Радиус поворота|Видимость  |Алгоритм|   
|-------|--------------------|------------------|-------------|---------------|-----------|--------|
|**23** |Ручная              |Да                |Квадратный   |Нет            |Бесконечная|B*      |

### CLI
```
--algorithm #Алгоитм поиска a* или b*
--grid      #Тип карты [big, obstacle, empty]
--start     #Точка старта
--finish    #Точка финиша
```

### Примеры запуска
```bash
python3 main.py --algorithm b* --grid big --start 1 1 --finish 13 13
```
<image src="./screenshots/Figure_1_b*.png" caption="B*">

```bash
python3 main.py --algorithm a* --grid big --start 1 1 --finish 13 13
```
<image src="./screenshots/Figure_1_a*.png" caption="A*">

```bash
python3 main.py --algorithm b* --grid obstacle --start 0 0 --finish 7 7
```
<image src="./screenshots/Figure_2_b*.png" caption="B*">