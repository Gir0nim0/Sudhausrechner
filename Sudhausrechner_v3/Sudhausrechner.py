import sys

from qtpy import QtWidgets

from ui.Sudhausrechner import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.exitButton.clicked.connect(exit)
        self.ui.shaButton.clicked.connect(self.calculateSha)
        self.ui.refraktometerButton.clicked.connect(self.calculateScheinRestextrakt)
        self.ui.refraktometerButton.clicked.connect(self.vergaerungsgrad)
        self.ui.refraktometerButton.clicked.connect(self.alkoholgehalt)
        self.ui.buttonFlaschenrechner.clicked.connect(self.flaschenrechner)

        # Sudhausausbeute berechnen

    def calculateSha(self):
        kg = self.ui.schuettung.text()
        grad_plato = self.ui.stammwuerze.text()
        ausschlagmenge = self.ui.ausschlagwuerze.text()

        # Formel Sudhausausbeute

        sha_result = float(grad_plato.replace(",", ".")) * float(ausschlagmenge.replace(",", ".")) / float(kg.replace(",", "."))
        self.ui.sha.setText(str(round(sha_result, 1))+ " %")

        # Scheinbarer Restextrakt berechnen

    def calculateScheinRestextrakt(self):
        wert_stammwuerze = self.ui.stammwuerzeRefrKorr.text()
        wert_refraktometer = self.ui.refrMessWert.text()

        # Umrechnung von Plato in Brix

        ra_stw = float(wert_stammwuerze.replace(",", ".")) * 1.04

        # Formel korrigierter scheinbarer Extraktgehalt in SG

        re_s = 1.0000 - 0.00085683 * float(ra_stw) + 0.0034941 * float(wert_refraktometer.replace(",", "."))

        # Umrechnung SG in Plato

        scheinbarer_restextrakt_plato = (re_s - 1) * 1000 / 4
        self.ui.resultSchRestExtrakt.setText(str(round(scheinbarer_restextrakt_plato, 1))+ "  ° P")

        # Scheinbarer Vergärungsgrad

    def vergaerungsgrad(self):
        wert_stammwuerze = self.ui.stammwuerzeRefrKorr.text()
        wert_refraktometer = self.ui.refrMessWert.text()
        ra_stw = float(wert_stammwuerze.replace(",", ".")) * 1.04
        re_s = 1.0000 - 0.00085683 * float(ra_stw) + 0.0034941 * float(wert_refraktometer.replace(",", "."))
        scheinbarer_restextrakt_plato = (re_s - 1) * 1000 / 4

        # Formel Scheinbarer Vergärungsgrad

        vg_s = (1 - float(scheinbarer_restextrakt_plato) / float(ra_stw)) * 100
        self.ui.resultSchVergaerungsgrad.setText(str(round(vg_s, 1)) + " %")

        # Alkoholgehalt

    def alkoholgehalt(self):
        wert_stammwuerze = self.ui.stammwuerzeRefrKorr.text()
        wert_refraktometer = self.ui.refrMessWert.text()
        ra_stw = float(wert_stammwuerze.replace(",", ".")) * 1.04
        re_s = 1.0000 - 0.00085683 * float(ra_stw) + 0.0034941 * float(wert_refraktometer.replace(",", "."))
        scheinbarer_restextrakt_plato = (re_s - 1) * 1000 / 4

        # Tatsächlicher Restextrakt

        re_t = 0.1808 * float(wert_stammwuerze.replace(",", ".")) + 0.8192 * float(scheinbarer_restextrakt_plato)

        # Alkoholgehalt in Gewichtsprozent

        alkohol_gewichtsprozent = (float(wert_stammwuerze.replace(",", ".")) - float(re_t)) / (2.0665 - 0.010665 * float(wert_stammwuerze.replace(",", ".")))

        # Dichte

        d = 261.1 / (261.53 - float(re_t))

        # Alkoholgehalt in Volumenprozent

        alkohol_volumenprozent = float(d) * float(alkohol_gewichtsprozent) / 0.794

        self.ui.resultAlkohol.setText("ca. " + str(round(alkohol_volumenprozent, 1)) + " %vol")

    def flaschenrechner(self):
        nulldreidrei = int(self.ui.inputAnzahl033L.text())
        nullfuenf = int(self.ui.inputAnzahl05L.text())
        nullsiebenfuenf = int(self.ui.inputAnzahl075L.text())
        eins = int(self.ui.inputAnzahl1L.text())

        result = (nulldreidrei * 0.33) + (nullfuenf * 0.5) + (nullsiebenfuenf * 0.75) + eins

        self.ui.flaschenrechnerResult.setText(str(round(result, 2)) + " L")


window = MainWindow()
window.show()
sys.exit(app.exec_())
