<script lang="ts">
	import DayView from '$lib/components/DayView.svelte';

	let { data }: { data: { selectedDate: string | null } } = $props();
</script>

<DayView selectedDate={data.selectedDate} />
