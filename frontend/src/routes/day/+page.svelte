<script lang="ts">
	let { data }: { data: { selectedDate: string | null } } = $props();
</script>

<h1 class="text-2xl font-semibold">Day Details</h1>

{#if data.selectedDate}
	<p>Showing events for: {data.selectedDate}</p>
{:else}
	<p>No date selected. Go back to calendar and choose a day.</p>
{/if}
