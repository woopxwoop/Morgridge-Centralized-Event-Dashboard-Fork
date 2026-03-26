<script lang="ts">
	import DayView from '$lib/components/DayView.svelte';

	let { data }: { data: { selectedDate: string | null; expandedEventId: number | null } } =
		$props();
</script>

<DayView selectedDate={data.selectedDate} expandedEventId={data.expandedEventId} />
