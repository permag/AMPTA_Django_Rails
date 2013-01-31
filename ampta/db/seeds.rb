# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ :name => 'Chicago' }, { :name => 'Copenhagen' }])
#   Mayor.create(:name => 'Emanuel', :city => cities.first)


User.delete_all
User.create(:first_name => "Per", 
            :last_name => "Magnusson", 
            :email => "pm222br@student.lnu.se",
            :password => "123456")

User.create(:first_name => "Uhno", 
            :last_name => "Johanssohn", 
            :email => "Bluhää@atrihs.seh",
            :password => "123456")