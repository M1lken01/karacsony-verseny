<template>
  <footer class="text-center pt-24 pb-4 bg-bg300 text-white">
    <div class="flex justify-center gap-8 flex-col md:flex-row">
      <div class="flex flex-col">
        <span class="font-bold">Navigation</span>
        <a class="p-1" href="#app">Intro</a>
        <a class="p-1" href="#gallery">Gallery</a>
        <a class="p-1" href="#about">About</a>
      </div>
      <div class="flex flex-col">
        <span class="font-bold">Made with ❤️ by</span>
        <a
          v-for="developer in developers"
          :key="developer.id"
          class="p-1"
          :href="developer.link"
          target="_blank"
          @mouseover="toggleHover(developer)"
          @mouseout="toggleHover(developer)"
        >
          {{ developer.hover ? developer.nickname : developer.fullName }}
        </a>
      </div>
    </div>
    <div class="p-8 px-8 flex justify-between flex-col-reverse gap-8 md:flex-row md:px-24">
      <div>&copy; 2023 <a href="https://github.com/M1lken01/karacsony-verseny">some Bolyai devs</a>. All rights reserved.</div>
      <div>
        <a href="https://github.com/M1lken01/karacsony-verseny" class="flex items-center justify-center">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="-2.5 -2.5 21 21" stroke="currentColor" class="h-7 w-7 mr-1">
            <path
              d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"
            ></path>
          </svg>
          Source Code
        </a>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'FooterSection',
  data() {
    return {
      developers: [
        { id: 1, nickname: 'm1lk3n01', fullName: 'Artner Milan', link: 'https://github.com/M1lken01', hover: false },
        { id: 2, nickname: 'McB0nd', fullName: 'Csendes Tamas', link: 'https://github.com/McB0nd', hover: false },
        { id: 3, nickname: 'Pingitzergggg', fullName: 'Pingtizer David', link: 'https://github.com/Pingitzergggg', hover: false },
      ],
    };
  },
  methods: {
    toggleHover(developer) {
      developer.hover = !developer.hover;
    },
  },
};
</script>
