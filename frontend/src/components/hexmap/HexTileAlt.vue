<template>
  <HexMap :columns="19" :rows="7" />
  <div class="hexagon"></div>
</template>

<style scoped>
.hexagon {
  margin-top: 104px;
  height: 104px; /* adjust to control the size  */
  aspect-ratio: 1 / cos(30deg);
  clip-path: polygon(50% -50%, 100% 50%, 50% 150%, 0 50%);
  background: #3b8686;
}

.hexagon:hover {
  background: red;
}
</style>
