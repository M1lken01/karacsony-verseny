<template>
  <section id="preview" class="flex flex-col min-h-screen gap-10 text-bg200 bg-fg500">
    <h2 class="section-title">Bemutató</h2>
    <div class="flex flex-1 flex-col md:flex-row gap-10 p-10 md:p-20">
      <div class="flex flex-1 bg-fg500">
        <iframe
          class="flex-1 rounded-md shadow-md"
          title="preview"
          frameborder="0"
          allowfullscreen
          mozallowfullscreen="true"
          webkitallowfullscreen="true"
          allow="autoplay; fullscreen; xr-spatial-tracking"
          xr-spatial-tracking
          execution-while-out-of-viewport
          execution-while-not-rendered
          web-share
          src="https://sketchfab.com/models/f8d7a5f3d7e54da983979ffca1163ddb/embed?autostart=1&ui_theme=dark&dnt=1"
        >
        </iframe>
      </div>
      <div class="flex flex-1 flex-col gap-10">
        <h3 class="preview-title">Építjük a Jövő Robotikus Tehetségeit!</h3>
        <p>
          Üdvözöljük a tehetségműhelyben, ahol fiatal tehetségeink robotikával és technológiával bővítik ismereteiket és szárnyalnak a versenyeken. Fedezze fel,
          hogyan alakult ki és fejlődött az elmúlt 7 év során, és ismerje meg a csapatunkat, akik már sikeresen képviselték iskolánkat különböző versenyeken!
        </p>
        <h3 class="preview-title">Milyen eszközökkel dolgoznak a diákok?</h3>
        <p>
          A tehetségműhelynek 7 darab Lego-robot készlete van. Ezek Ev3-as modellek. Nem a legújabbak, még 7 éve kaptuk őket pályázatok, illetve a Mobilis-SMR
          mentorprogram keretében. Most már lassan időszerű lesz a cseréjük. Egy-egy robot körülbelül 3 évet bír, ilyen mértékű igénybevétel mellett. A mi
          eszközeink ennek már a dupláját teljesítették.
        </p>
        <h3 class="preview-title">Amivel még foglalkozunk</h3>
        <p>
          A robotikával kapcsolatos elfoglaltságok kívül a tehetségműhely tagjai egyéb informatikai tevékenységekben is részt vehetnek, mint például
          prezentáció, vagy alkalmazás készítés, melyeknek célja mindig innovációs jellegűek. Az alábbi QR kód az egyik ilyen diákok által fejlesztett
          alkalmazásra vezet, aminek célja hogy segítsen az embereknek az energiatakarékoskodásban.
          <a href="https://drive.google.com/file/d/13h9SZMTXyJQ6mPFGXrJ1Ij3cbevUJmey/view?usp=drivesdk">
            <img src="@/assets/brand/qr-code.png" alt="QR Code" class="w-48 mt-4" />
          </a>
        </p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'PreviewSection',
};
</script>
