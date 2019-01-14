from scrayping import *
from predict import *
from predict2 import *

if __name__ == '__main__':
    flag = True
    page = 1
    BrandList = []
    NameList = []

    while flag:
        URL = 'https://www.fashion-press.net/snaps/sex/mens?page=' + str(page)
        soup = openURL(URL)
        snaps = soup.find_all(attrs={'class': 'fp_media_tile'})

        if len(snaps) != 0:  # 写真がある場合はブランドを取得
            tmpBrandList = getBrandList(snaps)
            BrandList.extend(tmpBrandList)
            NameList.extend(getNameList(snaps))
            print('get page' + str(page))
            page += 1

        else:  # 写真がない場合は終了
            flag = False
            print('END')

    df = pd.DataFrame(data=BrandList, index=NameList)  # pandasのDataFrame型に
    df.to_csv('StreetSnapMen.csv')
    # df = pd.read_csv('StreetSnapMen.csv', index_col = 0)

    brand = getuniqueList(df)
    brand_df = pd.DataFrame(index=list(brand.keys()),
                            data=list(brand.values()))
    brand_df = brand_df.drop(np.nan) # NAN　を削除
