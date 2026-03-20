<script lang="ts">
	import { allEvents } from '$lib/stores/events';
	import { toLocalIsoDate } from '$lib/utils/date';
	import {
		calendarReferenceDate,
		calendarSearchQuery,
		calendarStepMode,
		expandedDayEventId,
		pizzaOnlyFilter
	} from '$lib/stores/calendar-ui';
	import { buildDayViewEvents } from '$lib/features/events/day-view';
	import { getEventSearchMatches } from '$lib/features/events/utils';

	let { dayNumber, date }: { dayNumber: number; date: Date } = $props();

	const dateParam = $derived(toLocalIsoDate(date));
	const dayEvents = $derived(buildDayViewEvents($allEvents, dateParam));
	const normalizedQuery = $derived($calendarSearchQuery.trim().toLowerCase());
	const dayEventMatches = $derived(
		dayEvents.map((event) => ({
			event,
			isMatch: normalizedQuery
				? getEventSearchMatches(event, normalizedQuery, 'preview').length > 0
				: true
		}))
	);
	const hasPizzaEvent = $derived(dayEvents.some((event) => event.food));
	const shouldHighlightDayNumber = $derived($pizzaOnlyFilter && hasPizzaEvent);

	const MAX_VISIBLE_EVENTS = 3; // Max number of events to show in the day block before showing the count badge
	const visibleEvents = $derived(dayEventMatches.slice(0, MAX_VISIBLE_EVENTS));
	const extraEventCount = $derived(dayEvents.length - MAX_VISIBLE_EVENTS);

	function openDayView(): void {
		calendarReferenceDate.set(new Date(date));
		expandedDayEventId.set(null);
		calendarStepMode.set('day');
	}

	let touchRight = $state(false);
	let touchBottom = $state(false);
	let hoveredEventId = $state<number | -9999>(-9999);

function mouseHover(e: MouseEvent, id: number) {
    const btn = e.currentTarget as HTMLElement;
    const rect = btn.getBoundingClientRect();
    const tooltipWidth = 288;
	const height = 173;
    const gap = 8;
    
	const overflowsRight = rect.right + gap + tooltipWidth > window.innerWidth;
	const overflowsLeft = rect.left - gap - tooltipWidth < 0;
	const overflowsBottom = rect.bottom + height > window.innerHeight;

    if (overflowsRight && overflowsLeft) {
		touchRight = false; 
    } else if (overflowsRight) {
        touchRight = true; 
    } else {
		touchRight = false;
	}

	touchBottom = overflowsBottom;

	hoveredEventId = id;
}

function mouseLeave() {
    hoveredEventId = -9999; 
}
</script>

<div
	class="flex h-full w-full flex-col items-stretch justify-start gap-1 overflow-visible rounded border border-transparent transition-colors hover:bg-(--uwGrayLightest)"
>
	<div class="w-full px-1">
		<button
			type="button"
			class={`block w-full cursor-pointer text-center ${hasPizzaEvent ? 'font-medium' : ''} ${shouldHighlightDayNumber ? 'text-(--uwRed)' : ''}`}
			onclick={openDayView}
		>
			{dayNumber}
		</button>
	</div>

	<div class="w-full min-w-0 overflow-visible px-1">
		<div class="flex flex-col gap-1">
			{#each visibleEvents as entry (entry.event.id)}
				<div class="relative group w-full hover:z-[100]"> 
					<button
						type="button"
						onmouseenter={(e) => mouseHover(e, entry.event.id)}
						onmouseleave={mouseLeave}
						class={`box-border max-h-[250px] overflow-hidden w-full cursor-pointer rounded-lg border px-1 py-0.5 text-left text-[10px] leading-tight transition-colors hover:border-(--uwBlack) hover:bg-(--uwWhite) hover:text-(--uwBlack) ${
							normalizedQuery
								? entry.isMatch
									? 'border-(--uwRed) bg-(--uwWhite) text-(--uwGrayDark)'
									: 'border-transparent text-(--uwGrayDark)/45'
								: 'border-transparent text-(--uwGrayDark)'
						}`}
						
						onclick={(e) => {
							e.stopPropagation(); 
							calendarReferenceDate.set(new Date(date));
							expandedDayEventId.set(entry.event.id);
							calendarStepMode.set('day');
						}}
					>
						<span class="event-title block">
							{entry.event.eventTitle}
						</span>

						{#if hoveredEventId === entry.event.id}
							<div class="absolute pointer-events-auto 
										${touchRight ? 'z-50 right-full pr-2' : 'z-50 left-full pl-2'}
										${touchBottom ? 'z-50 bottom-0': 'z-50 top-0'}">
								<div class="box-border w-72 bg-white border border-gray-200 rounded-lg shadow-xl p-3 transition-all duration-200">
									<div class="space-y-2"> 
										<h3 class="text-sm font-bold">{entry.event.eventTitle} {#if entry.event.food}🍕{/if}</h3>
										<p class="mt-0.5 text-sm text-(--uwGrayDark)/75">{entry.event.eventLocation}</p>
										<p class="text-sm font-medium text-(--uwRedDark)">@ {entry.event.eventStartTime}</p>
										<p class="text-sm text-(--uwGrayDark)">
											{entry.event.eventDescription?.length > 100 
												? entry.event.eventDescription.slice(0, 100) + '...' 
												: entry.event.eventDescription}
										</p>
									</div>
								</div>
							</div>
						{/if}
					</button>

				</div> 
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
</div>

<style>
	.event-title {
		overflow: hidden;
		display: -webkit-box;
		-webkit-line-clamp: 2;
		-webkit-box-orient: vertical;
	}
</style>
