use orcl;
show tables;

select distinct company from car_com_wel;
select * from car_com_wel;

select company,welfare,sum(cnt)
 from car_com_wel
 where career='5년차'
 group by company,welfare
 order by 3 desc;

select company,welfare,cnt
 from car_com_wel
 where career='5년차' and company='강소기업'
 group by company,welfare
 order by 3 desc;

select * from (
 select company,welfare,cnt,
	    dense_rank() over (partition by company order by cnt desc) as wel_rank
        from car_com_wel
        where career='5년차'
        group by company,welfare ) temp
	where temp.wel_rank<=10
    order by 4;

select * from (
 select company,welfare,cnt,
	    row_number() over (partition by company order by cnt desc) as wel_rank
        from car_com_wel
        where career='5년차'
        group by company,welfare ) temp
	where temp.wel_rank<=5
    order by 1,4;

select welfare,count(welfare)
	from (select company,welfare,cnt,
					row_number() over (partition by company order by cnt desc) as wel_rank
			from car_com_wel
            where career='5년차'
            group by company,welfare ) temp
		where temp.wel_rank<=5
        group by welfare
        order by 2 desc;
        
select * from (
	select company,welfare,cnt,
			row_number() over (partition by company order by cnt desc) as wel_rank
		from car_com_wel
        where career='5년차' and welfare not in ('B17','H1','A1')
        group by company,welfare ) temp
	where wel_rank<=5 and welfare not in ('A5','B7')
    order by 1,4;
    
select welfare,count(welfare) from
	( select company,welfare,cnt,
				row_number() over (partition by company order by cnt desc) wel_rank
        from car_com_wel
        where career='5년차' and welfare not in ('B17','H1','A1')
        group by company,welfare ) temp
	where wel_rank<=5 and welfare not in ('A5','B7')
    group by welfare
    order by 2 desc;
    
select * from (
	select company,welfare,cnt,
			row_number() over (partition by company order by cnt desc) as wel_rank
		from car_com_wel
        where career='5년차' and welfare not in ('B17','H1','A1')
        group by company,welfare ) temp
	where wel_rank<=5 and welfare not in ('A5','B7') and welfare='H3';
    