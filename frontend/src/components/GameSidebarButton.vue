<script setup>
  import { RouterLink } from "vue-router"

  defineProps({
    subroute: String,
    tooltip: String
  })
</script>

<template>
  <router-link :to="{ name: subroute }" custom v-slot="{ navigate }">
    <button
      @click="navigate"
      role="link"
      :title="tooltip"
      :class="{ 'router-link-current': $router.currentRoute.value.name == subroute }"
    >
      <slot name="icon"></slot>
    </button>
  </router-link>
</template>

<style scoped>
  button {
    display: block;
    width: 100%;
    background: none;
    cursor: pointer;
    border: none;
    padding: 10px;
    /* padding-bottom: 30px; */
  }

  .router-link-current {
    color: var(--c-primary-tx);
    background-color: var(--c-secondary-bg);
    font-weight: 600;
  }

  button {
    position: relative;
  }

  button:hover {
    padding-bottom: 30px;
  }

  button::after {
    color: var(--c-primary-tx);
    content: attr(title);
    display: none;
    left: 50%;
    transform: translateX(-50%);
    position: absolute;
  }
  button:hover::after {
    display: block;
  }

  /*
color: inherit;

font: inherit;
cursor: pointer;

*/
</style>
