<script lang="ts">
export default {
    data() {
        return {
          heading: 'Dropdown 1',
          options: ['Option 1', 'Option 2'],
          selected: this.setSelected || 'Option 1',
          // selected: 'Option 1'
        }
    },
    props: {
      setSelected: String
    },
    emits: ['DD1Change']
}
</script>

<template>
  <h2>{{ heading }}</h2>
  <div>
    <select v-model="selected" @change="$emit('DD1Change', selected)" class="p-2">
      <option disabled value="">Please select one</option>
      <option v-for="option in options" :key="option">{{ option }}</option>
    </select>
  </div>
</template>
