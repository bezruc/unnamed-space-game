<script setup>
  import { computed, ref } from "vue"

  const { isVisible, operationName } = defineProps({
    isVisible: {
      type: Boolean,
      required: true,
      default: false
    },
    operationName: {
      required: true,
      type: String,
      validator(value) {
        return ["create", "join"].includes(value)
      }
    }
  })

  const fieldName = computed(() => {
    switch (operationName) {
      case "create":
        return "name"
      case "join":
        return "id"
      default:
        return ""
    }
  })

  let input = ref("")

  let isValid = ref(true)
  let validationMessage = ref("")
  const resetValidation = () => {
    validationMessage.value = ""
    isValid.value = true
  }

  const emit = defineEmits(["close-dialog", "submit-dialog"])
  const close = () => {
    resetValidation()
    input.value = ""
    emit("close-dialog")
  }
  const submit = () => {
    if (input.value.trim() === "") {
      validationMessage.value = "Input invalid: is empty or only whitespace"
      isValid.value = false
      return
    }
    emit("submit-dialog", input.value)
    resetValidation()
    input.value = ""
  }
</script>

<template>
  <div class="lobby-dialog" :class="{ 'is-visible': isVisible }">
    <div class="flex">
      <button @click="close" id="close">CLOSE</button>
      <div>{{ operationName.toLocaleUpperCase() }} SESSION</div>
      <input
        type="text"
        name="lobbyDialogInput"
        id="lobbyDialogInput"
        v-model="input"
        :placeholder="'Enter session ' + fieldName + '...'"
        minlength="1"
        :class="{ 'is-invalid': !isValid }"
      />
      <div class="validation-message" :class="{ 'is-invalid': !isValid }">
        {{ validationMessage }}
      </div>
      <button @click="submit">{{ operationName.toUpperCase() }}</button>
    </div>
  </div>
</template>

<style scoped>
  .lobby-dialog {
    --width: 400px;
    --height: 200px;
    width: var(--width);
    height: var(--height);
    background-color: var(--c-secondary-bg);
    position: absolute;
    left: calc(50% - var(--width) / 2);
    top: calc(50% - var(--height) / 2);
    padding: 1rem;
    display: none;
  }

  .flex {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-direction: column;
  }

  .is-visible {
    display: block;
  }

  button {
    display: block;
  }

  input.is-invalid {
    outline: crimson solid 2px;
  }

  .validation-message {
    visibility: hidden;
    color: crimson;
    font-weight: 600;
    height: 1.5em;
  }

  .validation-message.is-invalid {
    visibility: visible;
  }

  #close {
    align-self: flex-start;
  }
</style>
