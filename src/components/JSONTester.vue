<script lang="ts">

export default {
  props: {
    file: String,
    port: {
      type: Number,
      default: 8100
    }
  },
  data(): {
    json_string: string
  } {
    return {
      json_string: ''
    }
  },
  async created() {
    // async lifecycle functions shown in
    // https://stackoverflow.com/a/59311495/4376000
    try {
      var json_obj: JSON = JSON.parse('["No JSON yet"]')

      const response = await fetch(`http://localhost:${this.port}/${this.file}`)

      if (response.status === 200) {
        json_obj = await response.json()
        this.json_string = JSON.stringify(json_obj)
      } else {
        this.json_string = `HTTP request failed with status code ${response.status}`
      }
    } catch (error) {
      this.json_string = `An error occurred: ${error}`
    }
  }
}

</script>

<template>
  <h2 class="font-bold text-xl mt-6">JSON Loading Test</h2>
  <div class="px-4">{{ json_string }}</div>
</template>