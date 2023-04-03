<script setup lang="ts">
import DropdownCluster from './components/dropdown/DropdownCluster.vue'
import DropdownTest3 from './components/dropdown/DropdownTest3.vue'
import DropdownWrapper from './components/dropdown/DropdownWrapper.vue'
import JsonTester from './components/JSONTester.vue'
</script>

<script lang="ts">
const initial_options = ['a', 'b']

export default {
  data(): {
    dropdown3: string,
    input3: string
  } {
    return {dropdown3: '', input3: ''}
  }
}
</script>

<template>
  <div class="mx-20 my-10">
    <DropdownWrapper />
    <DropdownCluster />
    <br />
    <JsonTester file="tsconfig.json" />
    <!--JsonTester
      file="https://raw.githubusercontent.com/bskinn/sphobjinv/main/tests/resource/objects_attrs.json"
    /-->
    <br />
    <div>
      <DropdownTest3 v-model="dropdown3" :options="initial_options" />
      <p>Dropdown value is: {{ dropdown3 }}</p><br />
    </div>
    <div>
      <p>Value is: {{ input3 }}</p>
      <input v-model="input3" class="border-1"/>
    </div>
  </div>
</template>
