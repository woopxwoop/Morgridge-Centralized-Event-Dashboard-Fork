<script lang="ts">
	import Calendar from '$lib/components/Calendar.svelte';
	import DayView from '$lib/components/DayView.svelte';
	import { calendarReferenceDate, calendarStepMode } from '$lib/stores/calendar-ui';

	function toLocalIsoDate(value: Date): string {
		const year = value.getFullYear();
		const month = String(value.getMonth() + 1).padStart(2, '0');
		const day = String(value.getDate()).padStart(2, '0');
		return `${year}-${month}-${day}`;
	}

	const selectedDate = $derived(toLocalIsoDate($calendarReferenceDate));
</script>

{#if $calendarStepMode === 'day'}
	<div class="h-full w-full overflow-auto">
		<DayView {selectedDate} />
	</div>
{:else}
	<Calendar />
{/if}
