<template>
  <section id="more" class="grid grid-cols-1 md:grid-cols-2 min-h-screen bg-bg300 p-0">
    <div class="cross-img" id="img1"></div>
    <div class="cross-text">
      <h3 class="text-xl font-bold pb-4">Mit kell tudni a tehetségműhelyről?</h3>
      <p class="text-justify">
        A tehetségműhely már 7 éve működik. 2016-ban jött létre Kuklis József és Kovács Ádám tanár urak közreműködésével. Később csatlakozott még a
        témavezetőkhöz Stencinger Dóra tanárnő, majd Vinnai Zsolt tanár úr és legújabbként Kullai Viktória tanárnő. 2017-ben már indult iskolánkból csapat az
        FLL (FIRST Lego League) regionális versenyen, Győrben. Ezen a versenyen azóta is részt vesz iskolánk Block Breakers névre hallgató csapata. Azok a
        csapatok, akik erről a versenyről továbbjutottak, indulhattak a következő fordulóban, mely egészen a nemzetközi, világverseny szintjéig tart. Az utóbbi
        évben már más versenyeken is megmérettük magunkat. Így a tavalyi évben már volt csapatunk a WRO robotolimpián, illetve a Hajdúböszörményi robot olimpián
        is. Mindkét versenyen szépen szerepeltek a diákjaink.
      </p>
    </div>
    <div class="cross-text">
      <h3 class="text-xl font-bold pb-4">Kik vesznek részt a munkában?</h3>
      <p class="text-justify">
        A tehetségműhelyben vegyes dolgoztak és dolgoznak jelenleg is felsős és technikus diákok is. A célja, hogy megalapozzuk a diákok számára a robotikával
        kapcsolatos alapismereteket, melyeket későbbi tanulmányaik során is alkalmazni tudnak majd. A robotika tehetségműhely tagjai közül sokan folytatták
        szakirányú tanulmányaikat egyetemen, amit külön nagy sikerként könyvelünk el. Szeretnénk megjeleníteni a weblapon a jelenlegi tagjainkat és a már
        elballagott, tiszteletbeli tagjainkat. Jelenlegi tagok: Kovács András, Kilácskó Marcell, Manczal Péter, Szikra Károly, Sipos Máté, Élő Renáta, Kiss
        Bálint Róbert, Kovács Bendegúz Krisztián, Pingitzer Dávid, Somogyi Bence Sándor Tiszteletbeli tagok (akik legalább 4 éven át versenyeztek): Magyar
        Karolina Írisz, Fördős Gergő, Vecsei Ábel
      </p>
    </div>
    <div class="cross-img" id="img2"></div>
  </section>
</template>

<script>
export default {
  name: 'CrossSection',
};
</script>

<style scoped>
#img1 {
  background-image: url('../assets/media/szakkor1.jpg');
}

#img2 {
  background-image: url('../assets/media/szakkor2.jpg');
}
</style>
