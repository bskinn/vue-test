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

const initial_dd1: string = 'Option 1'

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
  methods: {
    set_dd2(key: string) {
      this.dropdown2_options = dropdown2_data[key]
      this.dropdown2 = dropdown2_data[key][0]
      this.dd2_key += 1
    }
  },
  data(): {
    dropdown1: string
    dropdown2: string
    dropdown2_options: Array<string>
    dd2_key: number
  } {
    return {
      dropdown1: initial_dd1,
      dropdown2: dropdown2_data[initial_dd1][0],
      dropdown2_options: dropdown2_data[initial_dd1],
      dd2_key: 0
    }
  }
}
</script>


<template>
  <h2 class="text-xl font-bold pb-4">This is an attempt at a container.</h2>
  <div class="pb-5">
    <DropdownTest1 :setSelected="dropdown1" @d-d1-change="set_dd2" />
  </div>
  <div class="pb-5">
    <DropdownTest2 :setSelected="dropdown2" :setOptions="dropdown2_options" :key="dd2_key" />
  </div>
</template>