# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ :name => 'Chicago' }, { :name => 'Copenhagen' }])
#   Mayor.create(:name => 'Emanuel', :city => cities.first)


User.delete_all
u1 = User.create(:first_name => "Per", 
                 :last_name => "Magnusson", 
                 :email => "pm222br@student.lnu.se",
                 :password => "123456")

u2 = User.create(:first_name => "Uhno", 
                 :last_name => "Johanssohn", 
                 :email => "Bluhää@atrihs.seh",
                 :password => "123456")

Project.delete_all
p1 = Project.create(:name => "Första projektet",
                    :description => "En text som beskriver ett projekt...",
                    :owner_id => u1.id)

p2 = Project.create(:name => "Andra projektet",
                    :description => "En text som beskriver det andra projektet...",
                    :owner_id => u1.id)


u1.projects << p1
u1.projects << p2
u2.projects << p1
