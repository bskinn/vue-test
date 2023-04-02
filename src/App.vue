<script setup lang="ts">
import DropdownCluster from './components/dropdown/DropdownCluster.vue'
import DropdownWrapper from './components/dropdown/DropdownWrapper.vue'
import JsonTester from './components/JSONTester.vue'
</script>

<template>
    <div class="mx-20 my-10">
      <DropdownWrapper />
      <DropdownCluster />
      <br />
      <JsonTester file="tsconfig.json"/>
    </div>
</template>
