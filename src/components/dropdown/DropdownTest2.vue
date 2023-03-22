<script lang="ts">

const defaultOptions: Array<String> = ['Option 1', 'Option 2']

export default {
    data() {
        return {
          heading: 'Dropdown 2',
          options: this.setOptions !== undefined ? (this.setOptions.length ? this.setOptions : defaultOptions) : defaultOptions,
          selected: this.setSelected || 'Option 1',
        }
    },
    props: {
      setSelected: String,
      setOptions: Array<String>
    }
}
</script>

<template>
  <h2>{{ heading }}</h2>
  <select v-model="selected">
    <option disabled value="">Please select one</option>
    <option v-for="option in options" :key="option">{{ option }}</option>
  </select>
</template>
