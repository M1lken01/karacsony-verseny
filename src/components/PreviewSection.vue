<template>
  <section id="preview" class="flex flex-col min-h-screen gap-10 text-bg200 bg-fg500">
    <h2 class="mx-8 mt-8 text-left text-2xl">Preview</h2>
    <div class="flex flex-1 flex-col md:flex-row gap-10 p-10 md:p-20">
      <div class="flex flex-1 bg-fg500">
        <iframe
          class="flex-1"
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
      <div class="flex-1">
        <h3 class="text-xl font-bold pb-4">titleee</h3>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
          quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
          cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
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
