def main():
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    weather_information_tem = [tem_date.get('temperature') for tem_date in weather_information]

    temper_ave = sum(weather_information_tem) / len(weather_information)
    print(temper_ave)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK¬)
    osaka_sta = [sta_date.get('station') for sta_date in weather_information
                 if sta_date["prefecture"] == "大阪府"
                 ]

    print(osaka_sta)

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    fukuoka_temperature = [fukuoka_tem_date['temperature'] for fukuoka_tem_date in weather_information
                           if fukuoka_tem_date['prefecture'] == '福岡県'
                           ]

    print(sum(fukuoka_temperature) / len(fukuoka_temperature))


if __name__ == '__main__':
    main()
