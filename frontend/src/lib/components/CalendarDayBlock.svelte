<script lang="ts">
	import { countEventsOnIsoDate } from '$lib/features/events/utils';
	import { filteredEvents } from '$lib/stores/events';
	import { toLocalIsoDate } from '$lib/utils/date';
	import {
		calendarReferenceDate,
		calendarStepMode,
		expandedDayEventId
	} from '$lib/stores/calendar-ui';

	let { dayNumber, date }: { dayNumber: number; date: Date } = $props();

	const dateParam = $derived(toLocalIsoDate(date));
	const visibleEventCount = $derived(countEventsOnIsoDate($filteredEvents, dateParam));

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
	{#if visibleEventCount > 0}
		<button
			type="button"
			class="cursor-pointer rounded-full bg-black px-1.5 py-0.5 text-[10px] leading-none text-white"
			onclick={openDayView}
		>
			{visibleEventCount}
		</button>
	{/if}
</div>
