def validate_df(df):
    """
    Проверяет DataFrame на:
    - наличие пропусков
    - корректность типов данных
    - при необходимости можно добавить другие проверки
    """
    # 1. Проверка пропусков
    missing = df.isnull().sum()
    if missing.any():
        print("Внимание! Есть пропуски в колонках:")
        print(missing[missing > 0])
    else:
        print("Пропусков нет")

    # 2. Проверка типов данных
    print("\nТипы данных колонок:")
    print(df.dtypes)

    # 3. Дополнительно можно проверить минимальные требования к столбцам
    required_cols = ['Age', 'Attrition', 'Department']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        print(f"Отсутствуют обязательные колонки: {missing_cols}")
    else:
        print("Все обязательные колонки присутствуют")
