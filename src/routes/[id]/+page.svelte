<script>
  import { goto } from "$app/navigation";
  import Chart from "$components/Chart.svelte";

  export let data;
  const { data: municipalities } = data;

  function navigateBack() {
    goto("/");
  }
</script>

<article class="space-y-4">
  <button
    class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-700 transition duration-300"
    on:click={navigateBack}
  >
    Zpět
  </button>

  <div>
    <h1 class="text-2xl font-bold">{municipalities.name}</h1>
    <p class="text-lg">Kraj: {municipalities.kraj}</p>
  </div>

  <Chart data={municipalities.votesPerCandidate} />
</article>
