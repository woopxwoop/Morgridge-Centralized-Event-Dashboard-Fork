<script lang="ts">
	import { filteredEvents } from '$lib/stores/events';
	import { toLocalIsoDate } from '$lib/utils/date';
	import {
		calendarReferenceDate,
		calendarStepMode,
		expandedDayEventId
	} from '$lib/stores/calendar-ui';
	import { buildDayViewEvents } from '$lib/features/events/day-view';

	let { dayNumber, date }: { dayNumber: number; date: Date } = $props();

	const dateParam = $derived(toLocalIsoDate(date));
	const dayEvents = $derived(buildDayViewEvents($filteredEvents, dateParam));

	const MAX_VISIBLE_EVENTS = 3; // Max number of events to show in the day block before showing the count badge
	const visibleEvents = $derived(dayEvents.slice(0, MAX_VISIBLE_EVENTS));
	const extraEventCount = $derived(dayEvents.length - MAX_VISIBLE_EVENTS);

	function openDayView(): void {
		calendarReferenceDate.set(new Date(date));
		expandedDayEventId.set(null);
		calendarStepMode.set('day');
	}
</script>

<div
	class="flex h-full w-full flex-col items-center justify-start gap-1 rounded transition-colors hover:bg-(--uwGrayLightest)"
>
	<button type="button" class="cursor-pointer px-1" onclick={openDayView}>
		{dayNumber}
	</button>

	<div class="flex flex-col gap-1 overflow-hidden">	
		{#each visibleEvents as event (event.id)}
			<button
				type = "button"
				class = "w-full cursor-pointer rounded-lg border border-transparent px-1 py-0.5 text-left text-[10px] leading-tight text-(--uwGrayDark) transition-colors hover:border-(--uwGrayLight) hover:bg-(--uwGrayLightest)"
				title={event.eventTitle}
				onclick={(e) => {
					e.stopPropagation(); // Prevent the day view from opening when clicking on an event
					calendarReferenceDate.set(new Date(date));
					expandedDayEventId.set(event.id);
					calendarStepMode.set('day');	
				}}
			>
			{event.eventTitle.length > 15 ? event.eventTitle.substring(0, 15) + '...' : event.eventTitle}
			</button>
		{/each}
	
		{#if extraEventCount > 0}
			<button
				type="button"
				class="cursor-pointer rounded-full bg-black px-1.5 py-0.5 text-[10px] leading-none text-white"
				onclick={(e) => {
					e.stopPropagation();
					openDayView();
				}}
			>
				+{extraEventCount} more
			</button>
		{/if}
	</div>
</div>
