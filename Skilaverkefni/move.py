"""
Skrifið forrit, move.py, sem spyr notanda um staðsetningu sýndarveru á x-ás í hnitakerfi og gerir síðan kleift að færa sýndarveruna
til hægri eða vinstri sem gefið er til kynna með stöfunum 'r'  eða 'l'.
Notandinn á að geta fært sýndarveruna eins oft og hann vill en ef inntakið er hvorki 'r'  né 'l' þá hættir forritið keyrslu.
Leiðbeiningar fyrir notandann eru skrifaðar á skjáinn í upphafi en staðsetning sýndarverunnar er sýnd (með 'o') í hverri ítrun.

Leyfilegt bil á x-ásnum, sem sýndarveran getur ferðast eftir, er frá 1 til 10 og gera má ráð fyrir að í upphafi slái notandinn inn tölu
sem er á þessu bili.  Ef sýndarveran er þegar staðsett á öðrum enda bilsins þá færist hún ekkert þegar reynt er að færa hana út fyrir bilið.

Við lausnina eigið þið eingöngu að nota aðferðir/efni sem fjallað er um í fyrstu 5 köflunum í kennslubókinni.
Leggið mikla áherslu á að lausnin ykkar sé læsileg.

Athugið eftirfarandi:

Tölurnar 1 og 10 sem afmarka bilið eiga að vera útfærðar með föstum. Fasti í Python er breyta hvers gildi á ekki að breytast í forriti.
Góð regla er að nota hástafi fyrir nöfn á föstum.  
Þið eigið að nota föll í útfærslunni á verkefninu.
Það er í lagi að aðalforritið ykkar innihaldi lykkjuna en meginmál lykkjunnar á að mestu að vera framkvæmt með fallaköllum.
Sjá dæmi um inntak/úttak hér fyrir neðan.  Úttakið ykkar á að líta nákvæmlega eins út.
"""
def make_line(x): # býr til línu of x-um og setur "o" á sama stað og int
    printer = ""
    for i in range(1,11):
        if i != x:
            printer += "x"
        elif i == x:
            printer += "o"
    return (printer)

def introduction():
    left = "l - for moving left"
    right = "r - for moving right"
    stop = "Any other letter for quitting"
    lrs = "\n" + left + "\n" + right + "\n" + stop
    return lrs

user_input = int(input("Input a position between 1 and 10: "))

if 11 > user_input > 0: # passar að input sé á milli 1 og 10
    line = make_line(user_input)
    print (line, introduction())
    while True:
        shift = str(input("Input your choice: "))
        move = shift.lower()
        if move == "l":
            if user_input > 1: # passar að "o" fari ekki útaf til vinstri
                user_input -= 1 # hreyfir til vinstri
            print (make_line(user_input))
        elif move == "r":
            if user_input < 10: # passar að "o" fari ekki útaf til hægri
                user_input += 1 # hreyfir til hægri
            print (make_line(user_input))
        else:
            print (make_line(user_input))
            break