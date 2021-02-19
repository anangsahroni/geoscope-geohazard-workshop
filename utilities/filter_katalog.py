"""Kumpulan fungsi untuk memfilter data katalog
"""
def filter_katalog_waktu(waktu_awal, waktu_akhir, waktu, longitude, \
                         latitude, kedalaman, magnitudo):
    """Fungsi untuk memfilter katalog berdasarkan waktu
    
    Parameters:
    waktu_awal : datetime.datetime
        Waktu awal untuk proses filter
    waktu_akhir : datetime.datetime
        Waktu akhir untuk proses filter
    waktu : list
        List yang berisi waktu kejadian
    longitude : list
        List yang berisi longitude
    latitude : list
        List yang berisi latitude
    kedalaman : list
        List yang berisi kedalaman
    magnitudo : list
        List yang berisi magnitudo
    
        
    Returns:
    waktu_hasil_filter : list
        List yang berisi waktu kejadian hasil filter
    longitude_hasil_filter : list
        List yang berisi longitude hasil filter
    latitude_hasil_filter : list
        List yang berisi latitude hasil filter
    kedalaman_hasil_filter : list
        List yang berisi kedalaman hasil filter
    magnitudo_hasil_filter : list
        List yang berisi magnitudo hasil filter
    """ 
        
    #katalog hasil_filter
    waktu_hasil_filter = []
    longitude_hasil_filter = []
    latitude_hasil_filter = []
    kedalaman_hasil_filter = []
    magnitudo_hasil_filter = []

    # mengumpulkan kolom menjadi satu `zip`
    katalog = zip(waktu, latitude, longitude, kedalaman, magnitudo)

    for t,lat,lon,ked,mag in katalog:
        # jika waktu lebih dari tanggal awal dan kurang dari tanggal akhir
        if t>waktu_awal and t<waktu_akhir:
            waktu_hasil_filter.append(t)
            longitude_hasil_filter.append(lon)
            latitude_hasil_filter.append(lat)
            kedalaman_hasil_filter.append(ked)
            magnitudo_hasil_filter.append(mag)
    
    print("Semua data",len(waktu))
    print("Data hasil_filter",len(waktu_hasil_filter))
    return waktu_hasil_filter, longitude_hasil_filter, latitude_hasil_filter, \
            kedalaman_hasil_filter, magnitudo_hasil_filter
