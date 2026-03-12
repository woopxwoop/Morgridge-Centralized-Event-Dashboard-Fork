<script lang="ts">
	import {
		buildCurrentWeekDays,
		buildMonthCalendarDays,
		CALENDAR_WEEKDAY_LABELS,
		chunkCalendarWeeks
	} from '$lib/features/calendar/view';
	import CalendarDayBlock from '$lib/components/CalendarDayBlock.svelte';
	import { calendarReferenceDate, calendarStepMode } from '$lib/stores/calendar-ui';

	const calendarDays = $derived(buildMonthCalendarDays($calendarReferenceDate));
	const weeks = $derived(chunkCalendarWeeks(calendarDays));
	const currentWeekDays = $derived(buildCurrentWeekDays($calendarReferenceDate));
</script>

<div class="h-full w-full">
	<table class="h-full w-full table-fixed border-collapse">
		<thead>
			<tr>
				{#each CALENDAR_WEEKDAY_LABELS as day}
					<th class="pb-4 font-medium">{day}</th>
				{/each}
			</tr>
		</thead>
		{#if $calendarStepMode === 'week'}
			<tbody>
				<tr>
					{#each currentWeekDays as day}
						<td class="p align-top">
							<div class={day.isCurrentMonth ? '' : 'opacity-40'}>
								<CalendarDayBlock date={day.date} dayNumber={day.dayNumber} />
							</div>
						</td>
					{/each}
				</tr>
			</tbody>
		{:else}
			<tbody class="h-full grid-rows-6">
				{#each weeks as week}
					<tr class="row-span-1">
						{#each week as day}
							<td class="p align-top">
								<div class={day.isCurrentMonth ? '' : 'opacity-40'}>
									<CalendarDayBlock date={day.date} dayNumber={day.dayNumber} />
								</div>
							</td>
						{/each}
					</tr>
				{/each}
			</tbody>
		{/if}
	</table>
</div>
