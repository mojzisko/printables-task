<script>
  import { goto } from "$app/navigation";

  export let data;

  let searchTerm = "";
  let showSuggestions = false;

  const { data: municipalities } = data;

  $: showSuggestions = searchTerm.length >= 2;

  $: filteredObecs =
    searchTerm.length >= 2
      ? municipalities
          .filter((obec) =>
            obec.name.toLowerCase().includes(searchTerm.toLowerCase())
          )
          .slice(0, 10) // Limit the number of suggestions
      : [];

  $: console.log("municipalities", municipalities);
  $: console.log("searchTerm", searchTerm);
</script>

<div
  class="relative"
  on:blur={() => setTimeout(() => (showSuggestions = false), 150)}
>
  <input
    type="text"
    placeholder="Search for an OBEC..."
    class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
    bind:value={searchTerm}
    on:focus={() => searchTerm.length >= 2 && (showSuggestions = true)}
  />

  {#if showSuggestions}
    <div
      class="absolute left-0 right-0 mt-1 max-h-60 overflow-auto border border-gray-200 bg-white z-10"
    >
      {#each filteredObecs as obec (`${obec.name}-${obec.id}`)}
        <div
          class="px-4 py-2 hover:bg-gray-100 cursor-pointer"
          on:click={goto(`/${obec.id}`)}
        >
          {obec.name} - {obec.kraj} - {obec.id}
        </div>
      {/each}
      {#if filteredObecs.length === 0}
        <div class="px-4 py-2">Kááámo promiň ale našel jsem kulový</div>
      {/if}
    </div>
  {/if}
</div>

<style>
  input:focus,
  .absolute {
    z-index: 10;
  }
</style>
