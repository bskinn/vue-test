<script lang="ts">

type DropdownData = {
  [key: string]: string[];
}

const dropdown2_data: DropdownData = {
  'Option 1': ['foo', 'bar'],
  'Option 2': ['quux', 'frob']
}

const initial_dd1 = 'Option 1'

export default {
  data(): {
    dropdown1: string
    dropdown1_options: Array<string>
    dropdown2: string
    // dropdown2_options: Array<string>
  } {
    return {
      dropdown1: initial_dd1,
      dropdown1_options: Object.keys(dropdown2_data),
      // dropdown2_options: dropdown2_data[initial_dd1],
      dropdown2: ''
    }
  },
  computed: {
    dropdown2_options(): Array<string> {
      return dropdown2_data[this.dropdown1]
    },
    dropdown2_options_list(): string {
      return this.dropdown2_options.join(', ')
    }
  }
}
</script>

<template>
  <h2 class="my-4 font-bold text-xl">Dropdown Cluster</h2>

  <div class="my-2">
    <select v-model="dropdown1" class="p-1.5">
      <option disabled value=''>Please select one</option>
      <option v-for="option in dropdown1_options" :key="option">{{ option }}</option>
    </select>
  </div>
  <div class="my-2">
    <select v-model="dropdown2" class="p-1.5">
      <option disabled value=''>Please select one</option>
      <option v-for="option in dropdown2_options" :key="option">{{ option }}</option>
    </select>
  </div>
  <div class="text-2xl shadow-lg p-1.5 pl-5 bg-green-200">{{ dropdown2_options_list }}</div>
</template>