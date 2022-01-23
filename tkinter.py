import tkinter as tk
import tkinter.messagebox as mbox


class Application(tk.Frame):

    def __init__(self, master=None):
        ''' init aplikasi '''

        tk.Frame.__init__(self, master)

        #deklarasi variabel yang akan di proses
        self.presnEnt = tk.StringVar()
        self.presnCalc = tk.StringVar()
        #Tugas
        self.tugasEnt = tk.StringVar()
        self.tugasCalc = tk.StringVar()
        #UTS
        self.utsEnt = tk.StringVar()
        self.utsCalc = tk.StringVar()
        #UAS
        self.uasEnt = tk.StringVar()
        self.uasCalc = tk.StringVar()
        #Total dan grade
        self.totalEnt = tk.StringVar()
        self.gradeCalc = tk.StringVar()

        #pasang frame utama
        self.grid()
        # =============
        # layout tampilan

        #label judul
        curRow = 1
        tk.Label(self, text='Hitung Rataan Nilai', pady=20) \
            .grid(row=curRow, column=0, columnspan=4)
        
        #presensi
        curRow += 1
        tk.Label(self, text='Presensi').grid(row=curRow)
        tk.Entry(self, width=5, textvariable=self.presnEnt) \
            .grid(row=curRow, column=1)
        tk.Label(self, text='10%').grid(row=curRow, column=2)
        tk.Entry(self, width=5, state=tk.DISABLED,
        justify=tk.RIGHT, textvariable=self.presnCalc) \
            .grid(row=curRow, column=3)

        #tugas
        curRow +=1
        tk.Label(self, text='Tugas').grid(row=curRow)
        tk.Entry(self, width=5, textvariable=self.tugasEnt) \
            .grid(row=curRow, column=1)
        tk.Label(self, text='20%').grid(row=curRow, column=2)
        tk.Entry(self, width=5, state=tk.DISABLED,
         justify=tk.RIGHT, textvariable=self.tugasCalc) \
            .grid(row=curRow, column=3)

        #uts
        curRow +=1
        tk.Label(self, text='UTS').grid(row=curRow)
        tk.Entry(self, width=5, textvariable=self.utsEnt) \
            .grid(row=curRow, column=1)
        tk.Label(self, text='30%').grid(row=curRow, column=2)
        tk.Entry(self, width=5, state=tk.DISABLED,
         justify=tk.RIGHT, textvariable=self.utsCalc) \
            .grid(row=curRow, column=3)
        
        #uas
        curRow +=1
        tk.Label(self, text='UAS').grid(row=curRow)
        tk.Entry(self, width=5, textvariable=self.uasEnt) \
            .grid(row=curRow, column=1)
        tk.Label(self, text='40%').grid(row=curRow, column=2)
        tk.Entry(self, width=5, state=tk.DISABLED,
         justify=tk.RIGHT, textvariable=self.uasCalc) \
            .grid(row=curRow, column=3)

        #ringkasan total dan grade
        #tugas
        curRow +=1
        tk.Label(self, text='Total Nilai').grid(row=curRow, column=2)
        tk.Entry(self, width=5, state=tk.DISABLED,
         justify=tk.RIGHT, textvariable=self.tugasCalc) \
            .grid(row=curRow, column=3)

        curRow +=1 
        tk.Label(self, text='Grade').grid(row=curRow, column=2)
        tk.Entry(self, width=5, state=tk.DISABLED,
         justify=tk.RIGHT, textvariable=self.gradeCalc) \
            .grid(row=curRow, column=3)

        curRow +=1
        butFrame = tk.Frame(self, pady=20)
        tk.Button(butFrame, text='Hitung', command=self.calc) \
            .grid(row=curRow, column=0)
        tk.Button(butFrame, text='Hapus', command=self.clear) \
            .grid(row=curRow, column=1)
        tk.Button(butFrame, text='Keluar', command=self.quit) \
            .grid(row=curRow, column=2)
        butFrame.grid(row=curRow, column=0, columnspan=4)

        def calc(self):
            ''' Hitung total dan grade '''

            try:
                presn = 0.1 * int(self.presnEnt.get())
                tugas = 0.2 * int(self.tugasEnt.get())
                uts = 0.3 * int(self.utsEnt.get())
                uas = 0.4 * int(self.uasEnt.get())

                assert 0 <= presn <= 10
                assert 0 <= tugas <= 20
                assert 0 <= uts <= 30
                assert 0 <= uas <= 40

            except:
                    mbox.showerror('Error', 'Entri dengan angka numerik 0-100')

            else:
                    total = presn + tugas + uts + uas
                    if total < 50:
                        grade = 'D'
                    elif total < 70:
                        grade = 'C'
                    elif total < 80:
                        grade = 'B'
                    else:
                        grade = 'A'

        def clear(self):
            ''' Hapus entrian kembali blank '''

            if mbox.askyesno('Confirm', 'Hapus Entrian?'):
                self.presnEnt.set('')
                self.presnCalc.set('')
                self.tugasEnt.set('')
                self.tugasCalc.set('')
                self.utsEnt.set('')
                self.utsCalc.set('')
                self.uasEnt.set('')
                self.uasCalc.set('')
                self.totalCalc.set('')
                self.gradeCalc.set('')

        def quit(self):
            ''' Override Quit '''
            if mbox.askyesno('Confirm', 'Keluar Dari Program?'):
                super().quit()

if __name__ == '__main__':
    app = Application()
    app.master.tittle('Hitung Rataan Nilai')
    app.mainloop()