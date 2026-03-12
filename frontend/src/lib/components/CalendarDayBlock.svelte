<script lang="ts">
	import { countEventsOnIsoDate } from '$lib/features/events/utils';
	import { filteredEvents } from '$lib/stores/events';
	import { toLocalIsoDate } from '$lib/utils/date';
	import { calendarReferenceDate, calendarStepMode } from '$lib/stores/calendar-ui';

	let { dayNumber, date }: { dayNumber: number; date: Date } = $props();

	const dateParam = $derived(toLocalIsoDate(date));
	const visibleEventCount = $derived(countEventsOnIsoDate($filteredEvents, dateParam));

	function openDayView(event: MouseEvent): void {
		event.preventDefault();
		calendarReferenceDate.set(new Date(date));
		calendarStepMode.set('day');
	}
</script>

<div class="flex h-full w-full flex-col items-center justify-start gap-1">
	<a class="px-1" href={`/day?date=${dateParam}`} onclick={openDayView}>{dayNumber}</a>
	{#if visibleEventCount > 0}
		<span class="rounded-full bg-black px-1.5 py-0.5 text-[10px] leading-none text-white">
			{visibleEventCount}
		</span>
	{/if}
</div>
