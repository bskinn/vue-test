<script setup lang="ts">
import DropdownCluster from './components/dropdown/DropdownCluster.vue'
import DropdownTest3 from './components/dropdown/DropdownTest3.vue'
import DropdownWrapper from './components/dropdown/DropdownWrapper.vue'
import JsonTester from './components/JSONTester.vue'
</script>

<script lang="ts">
const initial_options = ['a', 'b']
</script>

<template>
  <div class="mx-20 my-10">
    <DropdownWrapper />
    <DropdownCluster />
    <br />
    <JsonTester file="tsconfig.json" />
    <JsonTester
      file="https://raw.githubusercontent.com/bskinn/sphobjinv/main/tests/resource/objects_attrs.json"
    />
    <br />
    <DropdownTest3 :options="initial_options" />
  </div>
</template>
