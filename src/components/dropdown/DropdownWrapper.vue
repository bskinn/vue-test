<script setup lang="ts">
import DropdownTest1 from './DropdownTest1.vue'
import DropdownTest2 from './DropdownTest2.vue'
</script>


<script lang="ts">
type DropdownData = {
  [key: string]: string[];
}

const dropdown2_data: DropdownData = {
  'Option 1': ['foo', 'bar'],
  'Option 2': ['quux', 'frob']
}

export default {
  components: {
    DropdownTest1,
    DropdownTest2
  },
  // computed: {
  //   dropdown2_options(): Array<string> {
  //     return this.dropdown2_data[this.dropdown1] || []
  //   }
  // },
  watch: {
    dropdown1(newVal: string) {
      console.log(newVal)
      this.dropdown2_options = dropdown2_data[newVal]
      this.dropdown2 = dropdown2_data[newVal][0]
    }
  },
  data(): {
    dropdown1: string
    dropdown2: string
    dropdown2_options: Array<string>
  } {
    return {
      dropdown1: 'Option 1',
      dropdown2: '',
      dropdown2_options: dropdown2_data['Option 1']
    }
  }
}
</script>


<template>
  <h2>This is an attempt at a container.</h2>
  <DropdownTest1 :setSelected="dropdown1" />
  <DropdownTest2 :setSelected="dropdown2" :setOptions="dropdown2_options"/>
</template>