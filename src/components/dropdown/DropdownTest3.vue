<script lang="ts">
export default {
    data() {
        return {
          // heading: 'Dropdown 3',
          // options: ['Option 1', 'Option 2'],
          // selected: this.setSelected || 'Option 1',
          // selected: 'Option 1'
        }
    },
    props: {
      heading: {
        type: String,
        default: 'A Dropdown'
      },
      options: {
        type: Array<string>,
        default: ['Option 1', 'Option 2']
      },
      modelValue: {
        type: String,
        default: ''
      }
    },
    emits: ['update:modelValue'],
    methods: {
      handleChange(event: Event) {
        const target = event.target as HTMLSelectElement
        const value = target.value || ''
        this.$emit('update:modelValue', value)
      }
    }
}
</script>

<template>
  <h2>{{ heading }}</h2>
  <div>
    <select :value="modelValue" @change="handleChange" class="p-2">
      <option disabled value="">Please select one</option>
      <option v-for="option in options" :key="option">{{ option }}</option>
    </select>
  </div>
</template>
