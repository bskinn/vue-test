<script setup lang="ts">
import DropdownTest1 from './DropdownTest1.vue'
import DropdownTest2 from './DropdownTest2.vue'
</script>

<script lang="ts">
export default {
  components: {
    DropdownTest1,
    DropdownTest2
  },
  methods: {
    setDropdown2(newValue: string) {
      this.dropdown2 = newValue
      console.log(`Changed to ${newValue}`)
    }
  },
  data() {
    return {
      dropdown1: "Option 1",
      dropdown2: "Option 1"
    }
  }
}
</script>


<template>
  <h2>This is an attempt at a container.</h2>
  <DropdownTest1 :setSelected="dropdown1" @change="setDropdown2" />
  <DropdownTest2 :setSelected="dropdown2"/>
</template>