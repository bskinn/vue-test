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
  computed: {
    dropdown2_options(): Array<String> {
      return this.dropdown2_data["Option 1"] || []
    }
  },
  data() {
    return {
      dropdown1: "Option 1",
      dropdown2: "Option 1",
      dropdown2_data: {
        "Option 1": ['foo', 'bar'],
        "Option 2": ['quux', 'frob']
    }
    }
  }
}
</script>


<template>
  <h2>This is an attempt at a container.</h2>
  <DropdownTest1 :setSelected="dropdown1" />
  <DropdownTest2 :setSelected="dropdown2" :setOptions="dropdown2_options"/>
</template>