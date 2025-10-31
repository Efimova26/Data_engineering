# Data_engineering
Ссылка на датасет, выложенный на Google Drive https://drive.google.com/file/d/1BlN2qCu0WEVX6rHUBQw56wsljv7kqaJQ/view?usp=drive_link

**IBM HR Analytics: Employee Attrition & Performance**

**Описание:**
Датасет содержит данные о сотрудниках IBM с целью анализа текучести и производительности. Содержит ~1470 записей и 35 признаков, включая возраст, доход, удовлетворённость работой, стаж, переработки и др. Целевая переменная — Attrition (ушёл ли сотрудник).

**Задачи проекта:**

- Предсказание ухода сотрудников (классификация)
- Анализ факторов риска текучести
- Сегментация сотрудников по уровню риска
- Генерация HR-инсайтов для удержания персонала

**Ключевые факторы влияния на уход:**

- Сверхурочные (OverTime)
- Уровень дохода (MonthlyIncome)
- Удовлетворённость работой (JobSatisfaction)
- Стаж и продвижение (YearsAtCompany, YearsInCurrentRole)
- Расстояние до работы (DistanceFromHome)

**Особенности датасета:**

- Чистый, без пропусков
- Несбалансированная целевая переменная (~16% уходов)
- Идеален для обучения ML и HR-аналитике

**Ограничения:**

- Малый размер выборки (~1470 записей)
- Класс уходов несбалансирован
- Факторы внешней среды и динамика времени не учитываются

# Руководство по запуску
1. **Подготовка окружения**

Убедитесь, что ваше окружение data-eng активно:
```powershell
conda activate data-eng
```
2. **Установка необходимых компонентов**

Используйте Poetry для установки всех зависимостей проекта:
```powershell 
poetry install
```
3. **Настройка переменных**

Этот шаг требуется только при первом запуске.
Установите FILE_ID для доступа к данным:
```powershell 
conda env config vars set FILE_ID=1BlN2qCu0WEVX6rHUBQw56wsljv7kqaJQ
```
После этого повторно активируйте окружение, чтобы изменения вступили в силу:
```powershell
conda activate data-eng
```
4. **Запуск скрипта**

Теперь вы можете запустить скрипт загрузки данных:
```powershell
poetry run python data_loader.py
```
# Первые 10 строк даты

![Dataset head](images/images_1.jpg)

# Схема данных после предобработки (Dtypes)

Ниже представлена выдача типов данных (dtypes) DataFrame, подтверждающая успешное преобразование категориальных столбцов:

```python
Attrition                 category
BusinessTravel            category
DailyRate                    int64
Department                category
Education                    int64
EducationField            category
Gender                    category
HourlyRate                   int64
JobInvolvement               int64
JobLevel                     int64
JobRole                   category
MaritalStatus             category
MonthlyIncome                int64
MonthlyRate                  int64
NumCompaniesWorked           int64
OverTime                  category
PercentSalaryHike            int64
PerformanceRating            int64
RelationshipSatisfaction     int64
StockOptionLevel             int64
TotalWorkingYears            int64
TrainingTimesLastYear        int64
WorkLifeBalance              int64
YearsAtCompany               int64
YearsInCurrentRole           int64
YearsSinceLastPromotion      int64
YearsWithCurrManager         int64
dtype: object
```

## EDA

Для подробного анализа данных, выполненного в Jupyter Notebook, вы можете просмотреть его в nbviewer:

[Просмотреть EDA.ipynb в nbviewer](https://nbviewer.org/github/Efimova26/Data_engineering/blob/main/notebooks/EDA.ipynb)
