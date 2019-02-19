import codecs
import os

def Tupper(x,y):
    """ Tupper's self-referential formula.
    """
    return ( 0.5 < ( (y // 17) // ( 2 ** ( 17 * int(x) + int(y) % 17 ) ) ) % 2 )    


def tupperTXT(y):
    """ Prints Tupper's from starting y to y+16
    """ 


    with codecs.open("tupperTXT.txt", "w", "utf-8") as f:
        array = [ [ Tupper(x,z) for x in range(106) ] for z in range(y,y+17) ]
        for row in array:
            for value in row[::-1]:
                f.write("█"*value+' '*(not value))
            f.write(os.linesep)


if __name__ == "__main__":

    k = 960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719

    tupac = 222403917130227309614507700446867870101115834790138324607144860743012102121239987103271251739617881768621001470898328263812230067763893259290325670511324531977303674228130167785375329361441328377973308257102119810915550334876143176592615309585729767236229225656901324614072836724562950835390248549151486657172957029710437490832629495689990124847719364846327755191451423851633043680824094272703778997341852213849693368158216103059212715144778257342434924417320933077227978067957628168002019543477765165639469444080623316835390178687449038848


    tupperTXT(k)

