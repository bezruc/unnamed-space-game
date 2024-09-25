<script setup>
import { ref } from "vue"

defineProps({
  isEven: {
    type: Boolean,
    default: false
  }
})

const isMouseover = ref(false)
const isClicked = ref(false)
</script>

<template>
  <div class="hex" :class="{ even: isEven }">
    <div
      v-for="part in ['left', 'middle', 'right']"
      :key="part"
      @click="
        () => {
          isClicked = true
          isMouseover = false
        }
      "
      @mouseenter="() => (isMouseover = true)"
      @mouseleave="() => (isMouseover = false)"
      :class="[
        {
          'left-mouseover': !isClicked && isMouseover && part == 'left',
          'middle-mouseover': !isClicked && isMouseover && part == 'middle',
          'right-mouseover': !isClicked && isMouseover && part == 'right'
        },
        {
          'left-clicked': isClicked && part == 'left',
          'middle-clicked': isClicked && part == 'middle',
          'right-clicked': isClicked && part == 'right'
        },
        part
      ]"
    ></div>
  </div>
</template>

<style scoped>
.hex {
  float: left;
  margin-right: -26px;
  margin-bottom: -50px;
}
.hex .left {
  float: left;
  width: 0;
  border-right: 30px solid var(--c-primary-bg);
  border-top: 52px solid transparent;
  border-bottom: 52px solid transparent;
}
.hex .middle {
  float: left;
  width: 60px;
  height: 104px;
  background: var(--c-primary-bg);
}
.hex .right {
  float: left;
  width: 0;
  border-left: 30px solid var(--c-primary-bg);
  border-top: 52px solid transparent;
  border-bottom: 52px solid transparent;
}

.hex.even {
  margin-top: 53px;
}

.hex .left-mouseover {
  border-right: 30px solid var(--c-secondary-bg);
}

.hex .right-mouseover {
  border-left: 30px solid var(--c-secondary-bg);
}

.hex .middle-mouseover {
  background: var(--c-secondary-bg);
}

.hex .left-clicked {
  border-right: 30px solid var(--c-tertiary-bg);
}

.hex .right-clicked {
  border-left: 30px solid var(--c-tertiary-bg);
}

.hex .middle-clicked {
  background: var(--c-tertiary-bg);
}
</style>
