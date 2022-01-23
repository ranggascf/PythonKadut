class kuliah:
    insentif_beasiswa = 20000000
    def __init__(self, nama, usia, sks, ukt):
        self.nama = nama
        self.usia = usia
        self.sks  = sks * 150000
        self.ukt  = ukt
        self.bayaran_semesteran = 0
        self.pengurangan_biaya = 0
    def beasiswa(self):
        self.pengurangan_biaya += self.insentif_beasiswa
    def total_biaya_semesteran(self):
        return self.ukt + self.sks

